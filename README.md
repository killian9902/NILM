# NILM Project
* Currently data only from single house (H1)
* 'H1_AI_Dataset' - Preprocessd data

* 'Preprocess_1' - Process data into correct units
* 'Preprocess_2' - Process data into format for AI models (windowing/sequencing)
* 'Visual_Inspection' - Graph plotting to inspect distributions


* MLP BASE - very basic model
* MLP 1 - Includes train/test split & prints output,target randomly in test set
* MLP2 - ReLU & 1 hidden layer:
* MLP3 - LeakyReLU,  He initialisaiton, Layer normalisaiton & 1 hidden layer
* MLP Inspect - variance inspection
  * Plotting variance of forward and back signals using PyTorch hooks

* LSTM1 - very basic model (NOT FOCUSED ON)




## Dataset
* Data sourced from UK-DALE dataset
* Data source and info can be found below:
    * https://ukerc.rl.ac.uk/DC/cgi-bin/edc_search.pl/?WantComp=138
    * https://jack-kelly.com/data/

### Dataset structure
* house_1
    * channel_1
    * channel_2
    * channel_3
    * channel_4
    * channel_4_button_press
    *  ...
    *  ...
    *  ...
    * channel_53
    * channel_53_button_press
    * labels
    * mains
    * README
* house_2
    * 19 CHANNELS, labels, mains, README
* house_3
    * 5 CHANNELS, labels, mains, README
* house_4
    * 6 CHANNELS, labels, mains, README
* house_5
    * 25 CHANNELS, labels, mains, README
* metadata

'channel_x' records the watt consumption of appliance x, a monitor is attached to the device. 

'channel_x_button_press' records when device x is turned on or off, it is only available for some devices.

'labels' is a dictionary that states the name of every channel, i.e. house_1 'channel_4' is a laptop

'mains' is the house's total watt consumption


## Data Ingestion & Preprocessing
### Preprocess_1 (Feature Engineering)
1. Import data from UK-DALE DB
2. Select timeframe
    * Some devices were removed or added at different time points, so a timeframe is chosen where there is no changes 
3. Converts units from Watts/x_secs to Wh
4. Change to 15 min readings
    * Sum readings within every 15 min timeframe
5. Export clean data to (user's) directory

### Preprocess_2 (Formatting Data for AI Model)
1. Import clean data from (user's) directory
2. Window Labels dataframe, each row is the window moving up one timestamp
3. Group appliances based on similarities
4. Within each Appliance Group: sum total Wh and number of appliances on for each timestamp
5. Concatenate all Appliance Groups: one dataframe for sum, and one for count













