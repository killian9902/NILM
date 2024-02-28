# NILM Project
* Currently data only from single house (H1)
* 'H1_AI_Dataset' - Used to store preprocessd data (after Preprocess_1 & Preprocess_2)

* Currently working on 'MLP_Inspection' to get a better insight on how to improve models

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


## AI Model
### MLP_0
* Very basic model
* No test/training split
* Initially used to get a feel for data
* Now used as simple base/reference

### MLP_Print
* When training, the last epoch will print out some random (output,targets) in test set
* Used to understand how models are working

### MLP_Inspect
* Plotting variance of forward and back signals using PyTorch hooks

### MLP_1
* ReLU & 1 hidden layer

### MLP_2
* LeakyReLU, He initialisaiton, Layer normalisaiton & 1 hidden layer