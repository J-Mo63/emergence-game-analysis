# Emergence Game Analysis

This repository features an unsupervised analysis of emergent game data (which can be viewed [here](https://github.com/jonjondev/emergence-test-bed)), written in Python. It includes various tools for the pre-processing of game data and the generation of visualisations.

## Game Version 1 Visualisations

The first iteration of the experiment's codebase can be [viewed under the "v1" tag](https://github.com/jonjondev/emergence-test-bed/releases/tag/v1), which is defined in the below visuals as test `base_v1`. Each other test is denoted by the format of `<feature_name>_<value_change>` so for instance, a test increasing player speed by 20 would be written as `player_speed_+20`. The animated heatmaps and histograms are only generated for `base_v1` and the correlation matrices include all test results.

### Game World Location Heatmaps

<img src="visualisations/v1/heat_trees_spawned.gif" width="400"> <img src="visualisations/v1/heat_trees_harvested.gif" width="400"> <img src="visualisations/v1/heat_buildings_spawned.gif" width="400">

### Parameter Check Line Graphs

<img src="visualisations/v1/line_tree_pop.png" width="400"> <img src="visualisations/v1/line_dude_pop.png" width="400"> <img src="visualisations/v1/line_food_pop.png" width="400"> <img src="visualisations/v1/line_plant_pop.png" width="400"> <img src="visualisations/v1/line_building_pop.png" width="400">

### Event Time Histograms

<img src="visualisations/v1/hist_tree_growth.png" width="400"> <img src="visualisations/v1/hist_buildings_spawned.png" width="400"> <img src="visualisations/v1/hist_buildings_fixed.png" width="400">

### Correlation Matrices

<img src="visualisations/v1/summary_stat_correlation_matrix.png" width="400"> <img src="visualisations/v1/param_correlation_matrix.png" width="400">

## Game Version 2 Visualisations

The second iteration of the experiment's codebase can be [viewed under the "v2" tag](https://github.com/jonjondev/emergence-test-bed/releases/tag/v2), which is defined in the below visuals as test `base_v2`. It utilises the combination of features from the tests:
- dude_speed_+20
- plant_growth_rate_-5

Using this information, the plant growth rate was reduced from 15 seconds by 5 seconds and the speed of dudes was increased by 10 (only half of the amount it was increased by in the test). This resulted in the **preservation of food and tree populations** as well as the **reduction of tree growth to under 500 instances**.

### Parameter Check Line Graphs (Previous Tests)

<img src="visualisations/v1_2/line_tree_pop.png" width="400"> <img src="visualisations/v1_2/line_dude_pop.png" width="400"> <img src="visualisations/v1_2/line_food_pop.png" width="400"> <img src="visualisations/v1_2/line_plant_pop.png" width="400"> <img src="visualisations/v1_2/line_building_pop.png" width="400">

### Game World Location Heatmaps

<img src="visualisations/v1_2/heat_tree_spawned.gif" width="400"> <img src="visualisations/v1_2/heat_dude_harvested_resource_tree.gif" width="400"> <img src="visualisations/v1_2/heat_building_spawned.gif" width="400"> <img src="visualisations/v1_2/heat_dude_fixed_building.gif" width="400">

### Parameter Check Line Graphs (New Tests)

<img src="visualisations/v2/line_tree_pop.png" width="400"> <img src="visualisations/v2/line_dude_pop.png" width="400"> <img src="visualisations/v2/line_food_pop.png" width="400"> <img src="visualisations/v2/line_plant_pop.png" width="400"> <img src="visualisations/v2/line_building_pop.png" width="400">

## Game Version 3 Visualisations

The third iteration of the experiment's codebase can be [viewed under the "v3" tag](https://github.com/jonjondev/emergence-test-bed/releases/tag/v3), which is defined in the below visuals as test `base_v3`. It utilises the combination of features from the tests:
- tree_spawn_+0.4
- quarry_health_-30
- food_spawn_rate_-1

An issue identified in `base_v2` was that it created an overabundance of food. Using the information found, **this value was greatly reduced while preserving tree growth**.

### Parameter Check Line Graphs (Previous Tests)

<img src="visualisations/v2_3/line_tree_pop.png" width="400"> <img src="visualisations/v2_3/line_dude_pop.png" width="400"> <img src="visualisations/v2_3/line_food_pop.png" width="400"> <img src="visualisations/v2_3/line_plant_pop.png" width="400"> <img src="visualisations/v2_3/line_building_pop.png" width="400">

### Game World Location Heatmaps

<img src="visualisations/v2_3/heat_tree_spawned.gif" width="400"> <img src="visualisations/v2_3/heat_dude_harvested_resource_tree.gif" width="400"> <img src="visualisations/v2_3/heat_building_spawned.gif" width="400"> <img src="visualisations/v2_3/heat_dude_fixed_building.gif" width="400">

## Final Results

The final results for the analysis are shown below, highlighting all three base versions to illustrate the changes to the game's balance over time.

### Parameter Check Line Graphs of all Bases

<img src="visualisations/v3/line_tree_pop.png" width="400"> <img src="visualisations/v3/line_dude_pop.png" width="400"> <img src="visualisations/v3/line_food_pop.png" width="400"> <img src="visualisations/v3/line_plant_pop.png" width="400"> <img src="visualisations/v3/line_building_pop.png" width="400">
