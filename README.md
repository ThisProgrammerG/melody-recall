# Melody Recall: Remember the Notes

Test your memory recall by playing the sequence of notes. Played via mouse or numpad keys.

Small game built to experiment with ECS(EntityComponentSystem) and pygame's surface blending.




<img src="https://user-images.githubusercontent.com/116992225/232917994-96172743-9265-4f37-af3f-65418644e00a.png" width="700" />



Thoughts for the future:
* Move fully into ECS. 
  * VisibilityComponent 
  * ToggleComponent
  * TimerComponent
  * Query specific component combinations
* Join Position and Rect into one 
* Differentiate between Systems and Managers
* Entity should only be a number 
  * Does it even need to be a class?
* EventListeners composed of:
  * EventHandlers?