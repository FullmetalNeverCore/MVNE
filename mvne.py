import pygame 
from abc import ABC, abstractmethod


class MVNE_img(ABC):
    @abstractmethod
    def showimg(self):
        raise NotImplementedError  

class MVNE_text(ABC): 
    @abstractmethod
    def show_text(self):
        raise NotImplementedError  
    
    @abstractmethod
    def show_bbox(self):
        raise NotImplementedError
    

class MVNE_transitions_interface(ABC):

    @abstractmethod
    def fadein(self):
        raise NotImplementedError
    
    @abstractmethod
    def fadeout(self):
        raise NotImplementedError


class MVNE_classic_transitions(MVNE_transitions_interface):

    def __init__(self,starttime,transition_duration,obj) -> None:
        self.obj = obj
        self.elapsed_time = pygame.time.get_ticks() - starttime
        self.t_d = transition_duration
        self.s_t = starttime
        self.transition_progress = min(self.elapsed_time / self.t_d, 1)
        self.c_obj_surf = self.obj
        self.p_obj_surf = self.obj
        self.p_obj_alpha = 0
        self.c_obj_alpha = 255
    
    def fadein(self):
        # Calculate the alpha value of the text surface using linear interpolation
        c_obj_alpha = int(self.transition_progress * 255)
        self.c_obj_surf.set_alpha(c_obj_alpha)
    
    def fadeout(self):
        # Calculate the alpha value of the previous text surface using linear interpolation
        c_obj_alpha =  int((1 - self.transition_progress) * 255)
        self.c_obj_surf.set_alpha(c_obj_alpha)


    
class MVNE_classic_text_control(MVNE_text):
    def __init__(self,screen,text,WINDOW_SIZE,color=(255,255,255)) -> None:
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render(str(text), True, color)
        self.box_pos = pygame.Rect(0, WINDOW_SIZE[1] - 60, WINDOW_SIZE[0], 60)
        self.box_color = (0,0,0)
        self.text_position = self.text.get_rect()
        self.text_position.center = self.box_pos.center   
        self.c_obj_surf = self.text
        self.p_obj_surf = self.text
        self.p_obj_alpha = 0
        self.c_obj_alpha = 255   

    def show_bbox(self):
        pygame.draw.rect(self.screen, self.box_color, self.box_pos)

    def show_text(self):
        previous_text_position = self.p_obj_surf.get_rect()
        previous_text_position.center = self.box_pos.center
        self.screen.blit(self.p_obj_surf, previous_text_position)


        # Draw the current text surface with fadein effect
        current_text_position = self.c_obj_surf.get_rect()
        current_text_position.center = self.box_pos.center
        self.screen.blit(self.c_obj_surf, current_text_position)
        

class MVNE_classic_img(MVNE_img):
    def __init__(self,screen,img) -> None:
        self.screen = screen
        self.img = img 
    
    def showimg(self):
        self.screen.blit(self.img,(0,0))
