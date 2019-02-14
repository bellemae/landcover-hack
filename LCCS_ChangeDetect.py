LCCS_Categories = { # Note: AC made up the L1/L2 labels...

    # L1

    100: {'label': 'Vxx', 'desc': 'L1: Primarily Vegetated',},

    200: {'label': 'NVxx', 'desc': 'L1: Primarily Non-Vegetated',},

    # L2

    110: {'label': 'TVx', 'desc': 'L2: Terrestrial',},

    120: {'label': 'AVx', 'desc': 'L2: Aquatic or Regularly Flooded',},

    230: {'label': 'TNVx', 'desc': 'L2: Terrestrial',},

    240: {'label': 'ANVx', 'desc': 'L2: Aquatic or Regularly Flooded',},

    # L3

    111: {'label': 'CTV', 'desc': 'Cultivated & Managed Areas',},

    112: {'label': 'NTV', 'desc': '(Semi) Natural Vegetation',},

    123: {'label': 'CAV', 'desc': 'Cultivated Aquatic Areas',},

    124: {'label': 'NAV', 'desc': '(Semi) Natural Aquatic Vegetation',},

    235: {'label': 'AS', 'desc': 'Artifical Surfaces',},

    236: {'label': 'BS', 'desc': 'Bare Areas',},

    247: {'label': 'AW', 'desc': 'Artifical Waterbodies, Snow & Ice',},

    248: {'label': 'NW', 'desc': 'Natural Waterbodies, Snow & Ice',},

}

 

LCCS_Transition_Labels = {

    (111,111): {'desc':'stable', 'category': 0,},

    (111,112): {'desc':'afforestation', 'category': 1,},

    (111,123): {'desc':'change in agriculture', 'category': 1,},

    (111,124): {'desc':'afforestation', 'category': 1,},

    (111,235): {'desc':'urban expansion', 'category': -1,},

    (111,236): {'desc':'vegetation loss', 'category': -1,},

    (111,247): {'desc':'inundation', 'category': -1,},

    (111,248): {'desc':'inundation', 'category': -1,},

   

    (112,111): {'desc':'agricultural expansion', 'category': -1,},

    (112,112): {'desc':'stable', 'category': 0,},

    (112,123): {'desc':'agricultural expansion', 'category': -1,},

    (112,124): {'desc':'inundation', 'category': -1,},

    (112,235): {'desc':'urban expansion', 'category': -1,},

    (112,236): {'desc':'vegetation loss', 'category': -1,},

    (112,247): {'desc':'inundation', 'category': -1,},

    (112,248): {'desc':'inundation', 'category': -1,},

   

    (123,111): {'desc':'agriculture drainage', 'category': -1,},

    (123,112): {'desc':'afforestation/abandonment', 'category': 1,},

    (123,123): {'desc':'stable', 'category': 0,},

    (123,124): {'desc':'vegetation establishment', 'category': 1,},

    (123,235): {'desc':'urban expansion', 'category': -1,},

    (123,236): {'desc':'vegetation loss', 'category': -1,},

    (123,247): {'desc':'inundation', 'category': -1,},

    (123,248): {'desc':'inundation', 'category': -1,},

   

    (124,111): {'desc':'wetland drainage', 'category': -1,},

    (124,112): {'desc':'wetland loss', 'category': -1,},

    (124,123): {'desc':'wetland establishment', 'category': 1,},

    (124,124): {'desc':'stable', 'category': 0,},

    (124,235): {'desc':'urban expansion', 'category': -1,},

    (124,236): {'desc':'vegetation loss', 'category': -1,},

    (124,247): {'desc':'inundation', 'category': -1,},

    (124,248): {'desc':'inundation', 'category': -1,},

   

    (235,111): {'desc':'withdrawal of settlements', 'category': 1,},

    (235,112): {'desc':'withdrawal of settlements', 'category': 1,},

    (235,123): {'desc':'withdrawal of settlements', 'category': 1,},

    (235,124): {'desc':'withdrawal of settlements', 'category': 1,},

    (235,235): {'desc':'stable', 'category': 0,},

    (235,236): {'desc':'withdrawal of settlements', 'category': 1,},

    (235,247): {'desc':'inundation', 'category': -1,},

    (235,248): {'desc':'inundation', 'category': -1,},

   

    (236,111): {'desc':'agriculture expansion', 'category': 1,},

    (236,112): {'desc':'vegetation establishment', 'category': 1,},

    (236,123): {'desc':'vegetation establishment', 'category': 1,},

    (236,124): {'desc':'vegetation establishment', 'category': 1,},

    (236,235): {'desc':'urban expansion', 'category': -1,},

    (236,236): {'desc':'stable', 'category': 0,},

    (236,247): {'desc':'inundation', 'category': -1,},

    (236,248): {'desc':'inundation', 'category': -1,},

   

    (247,111): {'desc':'wetland drainage', 'category': -1,},

    (247,112): {'desc':'wetland drainage', 'category': -1,},

    (247,123): {'desc':'vegetation establishment', 'category': 1,},

    (247,124): {'desc':'vegetation establishment', 'category': 1,},

    (247,235): {'desc':'urban expansion', 'category': -1,},

    (247,236): {'desc':'wetland drainage', 'category': -1,},

    (247,247): {'desc':'stable', 'category': 0,},

    (247,248): {'desc':'wetland establishment', 'category': 1,},

   

    (248,111): {'desc':'wetland drainage', 'category': -1,},

    (248,112): {'desc':'vegetation encroachment', 'category': -1,},

    (248,123): {'desc':'wetland drainage', 'category': -1,},

    (248,124): {'desc':'vegetation encroachment', 'category': -1,},

    (248,235): {'desc':'urban expansion', 'category': -1,},

    (248,236): {'desc':'wetland drainage', 'category': -1,},

    (248,247): {'desc':'urban expansion', 'category': -1,},

    (248,248): {'desc':'stable', 'category': 0,},

}

 

# Add all the bazillions of L1 & L2 tuples (HACK!!!)

for a,av in LCCS_Categories.items():

    for b,bv in LCCS_Categories.items():

        if (a,b) not in LCCS_Transition_Labels:

            LCCS_Transition_Labels[(a,b)] = {'desc': av['desc']+' --> '+bv['desc'], 'category':None}

 

#LCCS_Transition_Labels

 

# Add short labels to LCCS_Transition_Labels based on abbreviations in LCCS_Categories

for a,b in LCCS_Transition_Labels:

    if a==b:

        LCCS_Transition_Labels[(a,b)]['label'] = LCCS_Categories[a]['label']

    else:

        LCCS_Transition_Labels[(a,b)]['label'] = "{a} -> {b}".format(a=LCCS_Categories[a]['label'],b=LCCS_Categories[b]['label'])

#LCCS_Transition_Labels

 

# Add (arbitrary) values to the LCCS_Transition_Labels for plotting

# Also create a reverse mapping

LCCS_ValueToTuple = {}

for idx,key in enumerate(sorted(LCCS_Transition_Labels)):

    LCCS_Transition_Labels[key]['val'] = idx

    LCCS_ValueToTuple[idx]=key

#LCCS_Transition_Labels

 

def LCCS_ChangeStats(da):

    counts = np.histogram(da, bins=[k for k in LCCS_ValueToTuple.keys()])

    # TODO: Expand on this! 

    return dict(zip(counts[1],counts[0]))

 

def LCCS_ChangeDetect(t1,t2,nodata=-1,name='LCCS_ChangeDetect_Result'):

   

    def _LCCS_ChangeDetect(a,b,nodata):

        change_type = (a,b)

        v = LCCS_Transition_Labels[change_type]['val'] if change_type in LCCS_Transition_Labels else nodata

        return v

 

    # Create some metadata to append

    metadata = {

        'nodata': nodata,

        # Copy CRS if available

        'crs': t1.crs if 'crs' in t1.attrs else t2.crs if 'crs' in t2.attrs else None,

        # Value labels

        'labels': {v['val']:v['label'] for l,v in LCCS_Transition_Labels.items()},

        # Value descriptions

        'descriptions': {v['val']:v['desc'] for l,v in LCCS_Transition_Labels.items()},

        # Just dumping all the lccs stuff into the metadata while we're here

        'lccs_dump': LCCS_Transition_Labels,

    }

   

    # Drop time if it exists (after adding it to metadata)

    if 'time' in t1.coords:

        metadata['time1'] = t1.time.values[0]

        t1 = t1.isel(time=0, drop=True)

    if 'time' in t2.coords:

        metadata['time2'] = t2.time.values[0]

        t2 = t2.isel(time=0, drop=True)

   

    #return xr.apply_ufunc(func,a,b, join='exact', vectorize=True, kwargs={'nodata':nodata}).unstack('xy')

    result = xr.apply_ufunc(

        _LCCS_ChangeDetect,

        t1,

        t2,

        join='exact',

        vectorize=True, # TODO: Test performance on larger datasets (True is faster for toy data)

        kwargs={'nodata':nodata}

    )

 

    # Add the metadata to attrs

    for (k,v) in metadata.items():

        result.attrs[k] = v

       

    result.attrs['stats'] = LCCS_ChangeStats(result)

 

    result.name = name

    return result #.astype(np.int16)

