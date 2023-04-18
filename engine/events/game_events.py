import pygame


EVENT_SWITCH_SCENE = pygame.event.custom_type()
EVENT_PLAY_AUDIO = pygame.event.custom_type()
EVENT_GLOW_EFFECT = pygame.event.custom_type()
EVENT_NOTE_PRESSED = pygame.event.custom_type()

def post_scene_switch_event(scene_type):
    pygame.event.post(pygame.event.Event(EVENT_SWITCH_SCENE, scene_type=scene_type))

def post_audio_event(audio_name, volume=1, loops=0):
    pygame.event.post(pygame.event.Event(EVENT_PLAY_AUDIO, audio_name=audio_name, volume=volume, loops=loops))

def post_glow_effect(entity, multiplier=1):
    pygame.event.post(pygame.event.Event(EVENT_GLOW_EFFECT, entity=entity, multiplier=multiplier))

def post_note_pressed(entity):
    pygame.event.post(pygame.event.Event(EVENT_NOTE_PRESSED, entity=entity))
