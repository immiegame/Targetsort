# TargetSortPython
 A python implementation of the quick sort algorithm for use in commercial video games and other projects.

 This quick sort algorithm has been modified slightly to support sorting to a target value.

 For example, let's say you were making a tower defense game and wanted to have custom targeting with your towers for stuff like close, first, etc. The first enemy would always be the closest to the end value for the track.

 Let e = 100 (the end value of the track in percentage)
 Let s = 0 (the start value of the track in percentage)
 Let a = [0, 9, 5, 6, 2, 1.2, 3, 90, 80, 55, 55.5, 55.75] (an array of values that correspond to the distance an enemy has covered on the track)

 By plugging in the value of 100 to this algorithm, the array will be ordered into closest to furthest, in which the enemy with distance of 90 will be at the start of the array, and the enemy with distance 0 will be at the end of the array.

 The quicksort algorithm was chosen because in realistic scenarios, it's very likely that the system will be dealing with hundreds, thousands, or even millions of enemies, and so a fast algorithm is necessary.
