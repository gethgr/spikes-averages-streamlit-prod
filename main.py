import streamlit as st
import numpy as np 
import pandas as pd

#import neo


st.set_page_config(
    page_title="Jumps Metrics App | SPESS",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="expanded",
    
)
st.sidebar.subheader("Please choose the propers files.")

col1, col2 = st.columns(2, gap='large')
#--- Insert the file with Spikes ---#
with col1:
    uploaded_spike_file = st.sidebar.file_uploader("Choose Spikes Excel File:")
    if uploaded_spike_file:
        df_spikes = pd.read_csv(uploaded_spike_file) #(uploaded_file, sep='\s+', skiprows=10, index_col = None)
        spikes_columns = len(df_spikes.columns)
        st.write('**Dataframe with Spikes - MU_Firings. There are {} Firings**'.format(spikes_columns))
        st.dataframe(df_spikes, use_container_width=True)
#---End of Insert the file with Spikes ---#

#--- Insert the file with EMG Volts Channels ---#
with col2:
    uploaded_emg_file = st.sidebar.file_uploader("Choose EMG Excel File:")
    if uploaded_emg_file:
        df_emg = pd.read_csv(uploaded_emg_file) #(uploaded_file, sep='\s+', skiprows=10, index_col = None)
        emg_columns = len(df_emg.columns) - 1 
        st.write('**Dataframe with Channels. There are {} Channels**'.format(emg_columns))
        st.dataframe(df_emg, use_container_width=True)
#---End of Insert the file with EMG Volts Channels ---#

#---  ---#
if uploaded_emg_file and uploaded_spike_file:
    @st.cache()
    def create_window_spike_df():
        my_dict1 = {"MU1_Firings":[], "dEMG.A_MU1 1 [V]":[], "dEMG.B_MU1 1 [V]":[], "dEMG.C_MU1 1 [V]":[], "dEMG.D_MU1 1 [V]":[]}
        my_dict2 = {"MU2_Firings":[], "dEMG.A_MU1 1 [V]":[], "dEMG.B_MU1 1 [V]":[], "dEMG.C_MU1 1 [V]":[], "dEMG.D_MU1 1 [V]":[]}
        my_dict3 = {"MU3_Firings":[], "dEMG.A_MU1 1 [V]":[], "dEMG.B_MU1 1 [V]":[], "dEMG.C_MU1 1 [V]":[], "dEMG.D_MU1 1 [V]":[]}
        my_dict4 = {"MU4_Firings":[], "dEMG.A_MU1 1 [V]":[], "dEMG.B_MU1 1 [V]":[], "dEMG.C_MU1 1 [V]":[], "dEMG.D_MU1 1 [V]":[]}
        my_dict5 = {"MU5_Firings":[], "dEMG.A_MU1 1 [V]":[], "dEMG.B_MU1 1 [V]":[], "dEMG.C_MU1 1 [V]":[], "dEMG.D_MU1 1 [V]":[]}

        #Iterate through every spike-time in Spikes file
        for spike in df_spikes.index:
            #Iterate through every time in EMG Volts Channels file
            for emgtime in df_emg.index:
                
                if spikes_columns >= 1:
                    #If Channel-time exists in window -10ms Spike-time +10ms, then keep spike-time and values of volts of channels
                    if df_spikes['MU1_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU1_Firings'][spike] + 0.010:
                        my_dict1["MU1_Firings"].append(df_spikes['MU1_Firings'][spike])
                        #my_dict1["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict1["dEMG.A_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.A 1 [V]'][emgtime])
                        my_dict1["dEMG.B_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.B 1 [V]'][emgtime])
                        my_dict1["dEMG.C_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.C 1 [V]'][emgtime])
                        my_dict1["dEMG.D_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.D 1 [V]'][emgtime])

                if spikes_columns >= 2:
                    if df_spikes['MU2_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU2_Firings'][spike] + 0.010:
                        my_dict2["MU2_Firings"].append(df_spikes['MU2_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict2["dEMG.A_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.A 1 [V]'][emgtime])
                        my_dict2["dEMG.B_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.B 1 [V]'][emgtime])
                        my_dict2["dEMG.C_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.C 1 [V]'][emgtime])
                        my_dict2["dEMG.D_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.D 1 [V]'][emgtime])
                
                if spikes_columns >= 3:
                    if df_spikes['MU3_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU3_Firings'][spike] + 0.010:
                        my_dict3["MU3_Firings"].append(df_spikes['MU3_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict3["dEMG.A_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.A 1 [V]'][emgtime])
                        my_dict3["dEMG.B_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.B 1 [V]'][emgtime])
                        my_dict3["dEMG.C_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.C 1 [V]'][emgtime])
                        my_dict3["dEMG.D_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.D 1 [V]'][emgtime])

                if spikes_columns >= 4:
                    if df_spikes['MU4_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU4_Firings'][spike] + 0.010:
                        my_dict4["MU4_Firings"].append(df_spikes['MU4_Firings'][spike])
                        my_dict4["dEMG.A_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.A 1 [V]'][emgtime])
                        my_dict4["dEMG.B_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.B 1 [V]'][emgtime])
                        my_dict4["dEMG.C_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.C 1 [V]'][emgtime])
                        my_dict4["dEMG.D_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.D 1 [V]'][emgtime])
                        
                if spikes_columns >= 5:
                    if df_spikes['MU5_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU5_Firings'][spike] + 0.010:
                        my_dict5["MU5_Firings"].append(df_spikes['MU5_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict5["dEMG.A_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.A 1 [V]'][emgtime])
                        my_dict5["dEMG.B_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.B 1 [V]'][emgtime])
                        my_dict5["dEMG.C_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.C 1 [V]'][emgtime])
                        my_dict5["dEMG.D_MU1 1 [V]"].append(df_emg['R VASTUS LATERALIS: dEMG.D 1 [V]'][emgtime])


        return my_dict1, my_dict2, my_dict3, my_dict4, my_dict5
    
    my_dict1, my_dict2, my_dict3, my_dict4, my_dict5 = create_window_spike_df()
    
    firing1, firing2, firing3, firing4, firing5 = st.tabs(["MU1_Firings", "MU2_Firings", "MU3_Firings","MU4_Firings","MU5_Firings"])
    #---- Start Firing 1 ----#
    with firing1:
        #if st.button('Calculate Firing 1'):
    
        df_from_my_dict1 = pd.DataFrame(my_dict1)
        st.write('#')
        # st.write('**Dataframe Window -10/+10 Spike Times Vertical**', len(df_from_my_dict1.columns))
        # st.dataframe(df_from_my_dict1, use_container_width=True)

        df_split_pivot = df_from_my_dict1.copy()
        df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict1.index, 
                        columns='MU1_Firings', 
                        values=['dEMG.A_MU1 1 [V]', 'dEMG.B_MU1 1 [V]', 'dEMG.C_MU1 1 [V]', 'dEMG.D_MU1 1 [V]'])
        df_from_my_dict1 = df_from_my_dict1.unstack(level=0)
    
        df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
        df_split_pivot['mean_A'] = df_split_pivot['dEMG.A_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_B'] = df_split_pivot['dEMG.B_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_C'] = df_split_pivot['dEMG.C_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_D'] = df_split_pivot['dEMG.D_MU1 1 [V]'].mean(axis=1)
        
        df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()

        with st.expander("Show Dataframes", expanded=True):
            col1, col2 = st.columns([1,3])
            with col1:
                st.write("#")
                st.write('**Dataframe Means Values for every channel.**')
                st.write(df_split_pivot_means,  use_container_width=True)

                st.download_button(
                            label="Export Means Datatable",
                            data=df_split_pivot_means.to_csv(),
                            file_name='file.csv',
                            mime='text/csv',
                        )
            with col2:
                st.write("#")
                st.write('**Dataframe Split values horizontal, there are {} columns**'.format(len(df_split_pivot.columns)))
                st.dataframe(df_split_pivot, use_container_width=True)
            
        st.write("---")
        st.subheader("**Charts for every mean value**")
        col1, col2  = st.columns(2, gap="large")
        with col1:
            st.write("Mean value for Channel A.")
            st.bar_chart(df_split_pivot_means['mean_A'])
            st.write("Mean value for Channel C.")
            st.bar_chart(df_split_pivot_means['mean_C'])            
        with col2:
            st.write("Mean value for Channel B.")
            st.bar_chart(df_split_pivot_means['mean_B'])
            st.write("Mean value for Channel D.")
            st.bar_chart(df_split_pivot_means['mean_D'])
       
    #---- End of Start Firing 1 ----#

    #---- Start Firing 2 ----#
    with firing2:
        #if st.button('Calculate Firing 2'):   
        df_from_my_dict2 = pd.DataFrame(my_dict2)
        st.write('#')
        #st.write('**Dataframe Window -10/+10 Spike Times Vertical**', len(df_from_my_dict2.columns))
        #st.dataframe(df_from_my_dict2, use_container_width=True)

        df_split_pivot = df_from_my_dict2.copy()
        df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict2.index, 
                        columns='MU2_Firings', 
                        values=['dEMG.A_MU1 1 [V]', 'dEMG.B_MU1 1 [V]', 'dEMG.C_MU1 1 [V]', 'dEMG.D_MU1 1 [V]'])
        df_from_my_dict2 = df_from_my_dict2.unstack(level=0)
    
        df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
        df_split_pivot['mean_A'] = df_split_pivot['dEMG.A_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_B'] = df_split_pivot['dEMG.B_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_C'] = df_split_pivot['dEMG.C_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_D'] = df_split_pivot['dEMG.D_MU1 1 [V]'].mean(axis=1)
        
        df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()

        with st.expander("Show Dataframes", expanded=True):
            col1, col2 = st.columns([1,3])
            with col1:
                st.write("#")
                st.write('**Dataframe Means Values for every channel.**')
                st.write(df_split_pivot_means,  use_container_width=True)

                st.download_button(
                            label="Export Means Datatable",
                            data=df_split_pivot_means.to_csv(),
                            file_name='file.csv',
                            mime='text/csv',
                        )
            with col2:
                st.write("#")
                st.write('**Dataframe Split values horizontal, there are {} columns**'.format(len(df_split_pivot.columns)))
                st.dataframe(df_split_pivot, use_container_width=True)
        
        st.write("---")
        st.subheader("**Charts for every mean value**")
        col1, col2  = st.columns(2, gap="large")
        with col1:
            st.write("Mean value for Channel A.")
            st.bar_chart(df_split_pivot_means['mean_A'])
            st.write("Mean value for Channel C.")
            st.bar_chart(df_split_pivot_means['mean_C'])            
        with col2:
            st.write("Mean value for Channel B.")
            st.bar_chart(df_split_pivot_means['mean_B'])
            st.write("Mean value for Channel D.")
            st.bar_chart(df_split_pivot_means['mean_D'])

    #---- End of Start Firing 2 ----#

    #---- Start Firing 3 ----#
    with firing3:
        #if st.button('Calculate Firing 3'):   
        df_from_my_dict3 = pd.DataFrame(my_dict3)
        st.write('#')
        #st.write('**Dataframe Window -10/+10 Spike Times Vertical**', len(df_from_my_dict3.columns))
        #st.dataframe(df_from_my_dict3, use_container_width=True)

        df_split_pivot = df_from_my_dict3.copy()
        df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict3.index, 
                        columns='MU3_Firings', 
                        values=['dEMG.A_MU1 1 [V]', 'dEMG.B_MU1 1 [V]', 'dEMG.C_MU1 1 [V]', 'dEMG.D_MU1 1 [V]'])
        df_from_my_dict3 = df_from_my_dict3.unstack(level=0)
    
        df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
        df_split_pivot['mean_A'] = df_split_pivot['dEMG.A_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_B'] = df_split_pivot['dEMG.B_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_C'] = df_split_pivot['dEMG.C_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_D'] = df_split_pivot['dEMG.D_MU1 1 [V]'].mean(axis=1)
        
        df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()

        with st.expander("Show Dataframes", expanded=True):
            col1, col2 = st.columns([1,3])
            with col1:
                st.write("#")
                st.write('**Dataframe Means Values for every channel.**')
                st.write(df_split_pivot_means,  use_container_width=True)

                st.download_button(
                            label="Export Means Datatable",
                            data=df_split_pivot_means.to_csv(),
                            file_name='file.csv',
                            mime='text/csv',
                        )
            with col2:
                st.write("#")
                st.write('**Dataframe Split values horizontal, there are {} columns**'.format(len(df_split_pivot.columns)))
                st.dataframe(df_split_pivot, use_container_width=True)
        
        st.write("---")
        st.subheader("**Charts for every mean value**")
        col1, col2  = st.columns(2, gap="large")
        with col1:
            st.write("Mean value for Channel A.")
            st.bar_chart(df_split_pivot_means['mean_A'])
            st.write("Mean value for Channel C.")
            st.bar_chart(df_split_pivot_means['mean_C'])            
        with col2:
            st.write("Mean value for Channel B.")
            st.bar_chart(df_split_pivot_means['mean_B'])
            st.write("Mean value for Channel D.")
            st.bar_chart(df_split_pivot_means['mean_D'])

    #---- End of Start Firing 3 ----#

    #---- Start Firing 4 ----#
    with firing4:
        #if st.button('Calculate Firing 4'):   
        df_from_my_dict4 = pd.DataFrame(my_dict4)
        st.write('#')
        #st.write('**Dataframe Window -10/+10 Spike Times Vertical**', len(df_from_my_dict4.columns))
        #st.dataframe(df_from_my_dict4, use_container_width=True)

        df_split_pivot = df_from_my_dict4.copy()
        df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict4.index, 
                        columns='MU4_Firings', 
                        values=['dEMG.A_MU1 1 [V]', 'dEMG.B_MU1 1 [V]', 'dEMG.C_MU1 1 [V]', 'dEMG.D_MU1 1 [V]'])
        df_from_my_dict4 = df_from_my_dict4.unstack(level=0)
    
        df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
        df_split_pivot['mean_A'] = df_split_pivot['dEMG.A_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_B'] = df_split_pivot['dEMG.B_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_C'] = df_split_pivot['dEMG.C_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_D'] = df_split_pivot['dEMG.D_MU1 1 [V]'].mean(axis=1)
        
        df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()

        with st.expander("Show Dataframes", expanded=True):
            col1, col2 = st.columns([1,3])
            with col1:
                st.write("#")
                st.write('**Dataframe Means Values for every channel.**')
                st.write(df_split_pivot_means,  use_container_width=True)

                st.download_button(
                            label="Export Means Datatable",
                            data=df_split_pivot_means.to_csv(),
                            file_name='file.csv',
                            mime='text/csv',
                        )
            with col2:
                st.write("#")
                st.write('**Dataframe Split values horizontal, there are {} columns**'.format(len(df_split_pivot.columns)))
                st.dataframe(df_split_pivot, use_container_width=True)
        
        st.write("---")
        st.subheader("**Charts for every mean value**")
        col1, col2  = st.columns(2, gap="large")
        with col1:
            st.write("Mean value for Channel A.")
            st.bar_chart(df_split_pivot_means['mean_A'])
            st.write("Mean value for Channel C.")
            st.bar_chart(df_split_pivot_means['mean_C'])            
        with col2:
            st.write("Mean value for Channel B.")
            st.bar_chart(df_split_pivot_means['mean_B'])
            st.write("Mean value for Channel D.")
            st.bar_chart(df_split_pivot_means['mean_D'])

    #---- End of Start Firing 4 ----#

    #---- Start Firing 5 ----#
    with firing5:
        #if st.button('Calculate Firing 5'):   
        df_from_my_dict5 = pd.DataFrame(my_dict5)
        st.write('#')
        #st.write('**Dataframe Window -10/+10 Spike Times Vertical**', len(df_from_my_dict5.columns))
        #st.dataframe(df_from_my_dict5, use_container_width=True)

        df_split_pivot = df_from_my_dict5.copy()
        df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict5.index, 
                        columns='MU5_Firings', 
                        values=['dEMG.A_MU1 1 [V]', 'dEMG.B_MU1 1 [V]', 'dEMG.C_MU1 1 [V]', 'dEMG.D_MU1 1 [V]'])
        df_from_my_dict5 = df_from_my_dict5.unstack(level=0)
    
        df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
        df_split_pivot['mean_A'] = df_split_pivot['dEMG.A_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_B'] = df_split_pivot['dEMG.B_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_C'] = df_split_pivot['dEMG.C_MU1 1 [V]'].mean(axis=1)
        df_split_pivot['mean_D'] = df_split_pivot['dEMG.D_MU1 1 [V]'].mean(axis=1)
        
        df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()

        with st.expander("Show Dataframes", expanded=True):
            col1, col2 = st.columns([1,3])
            with col1:
                st.write("#")
                st.write('**Dataframe Means Values for every channel.**')
                st.write(df_split_pivot_means,  use_container_width=True)

                st.download_button(
                            label="Export Means Datatable",
                            data=df_split_pivot_means.to_csv(),
                            file_name='file.csv',
                            mime='text/csv',
                        )
            with col2:
                st.write("#")
                st.write('**Dataframe Split values horizontal, there are {} columns**'.format(len(df_split_pivot.columns)))
                st.dataframe(df_split_pivot, use_container_width=True)
            
        st.write("---")
        st.subheader("**Charts for every mean value**")
        col1, col2  = st.columns(2, gap="large")
        with col1:
            st.write("Mean value for Channel A.")
            st.bar_chart(df_split_pivot_means['mean_A'])
            st.write("Mean value for Channel C.")
            st.bar_chart(df_split_pivot_means['mean_C'])            
        with col2:
            st.write("Mean value for Channel B.")
            st.bar_chart(df_split_pivot_means['mean_B'])
            st.write("Mean value for Channel D.")
            st.bar_chart(df_split_pivot_means['mean_D'])

    #---- End of Start Firing 5 ----#











    #df_from_my_dict2 = pd.DataFrame(my_dict2)

        
    # st.write('**Dataframe Window -10/+10 Spike Times Vertical FOR Dict2**', len(df_from_my_dict2.columns))
    # st.dataframe(df_from_my_dict2, use_container_width=True)

    #d = d.set_index('Spike')
        

    #
    
    
    # #st.bar_chart(df_split_pivot_means)
    # st.write("#")
    # col1, col2 , col3, col4 = st.columns(4, gap="large")
    # with col1:
    #     st.bar_chart(df_split_pivot_means['mean_A'])

    # with col2:
    #     st.bar_chart(df_split_pivot_means['mean_B'])
    
    # with col3:
    #     st.bar_chart(df_split_pivot_means['mean_C'])
    # with col4:
    #     st.bar_chart(df_split_pivot_means['mean_D'])
        




# signal = neo.AnalogSignal(np.array([signal1, signal2]).T, units='mV',
#                                sampling_rate=10/ms) 



# stavg = spike_triggered_average(signal, [spiketrain1, spiketrain2],
#                                 (-5 * ms, 10 * ms)) 


