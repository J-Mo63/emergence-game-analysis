# Emergence Game Analysis

This repository features an unsupervised analysis of emergent game data (which can be viewed [here](https://github.com/J-Mo63/emergence-test-bed)), written in Python. It includes various tools for the pre-processing of game data and the generation of visualisations.

## Game Version 1 Visualisations

The first iteration of the experiment's codebase can be [viewed under the "v1" tag](https://github.com/J-Mo63/emergence-test-bed/releases/tag/v1), which is defined in the below visuals as test `base_v1`. Each other test is denoted by the format of `<feature_name>_<value_change>` so for instance, a test increasing player speed by 20 would be written as `player_speed_+20`. The animated heatmaps and histograms are only generated for `base_v1` and the correlation matrices include all test results.

### Game World Location Heatmaps

<img src="visualisations/v1/heat_trees_spawned.gif" width="400"> <img src="visualisations/v1/heat_trees_harvested.gif" width="400"> <img src="visualisations/v1/heat_buildings_spawned.gif" width="400">

### Parameter Check Line Graphs

<img src="visualisations/v1/line_tree_pop.png" width="400"> <img src="visualisations/v1/line_dude_pop.png" width="400"> <img src="visualisations/v1/line_food_pop.png" width="400"> <img src="visualisations/v1/line_plant_pop.png" width="400"> <img src="visualisations/v1/line_building_pop.png" width="400">

### Event Time Histograms

<img src="visualisations/v1/hist_tree_growth.png" width="400"> <img src="visualisations/v1/hist_buildings_spawned.png" width="400"> <img src="visualisations/v1/hist_buildings_fixed.png" width="400">

### Correlation Matrices

<img src="visualisations/v1/summary_stat_correlation_matrix.png" width="400"> <img src="visualisations/v1/param_correlation_matrix.png" width="400">