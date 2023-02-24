import streamlit as st
import numpy as np 
import pandas as pd
#import neo

st.set_page_config(
    page_title="Spikes Averages Values",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

st.sidebar.subheader("Please choose the propers files.")

col1, col2 = st.columns(2, gap='large')
#--- Insert the file with Spikes ---#
with col1:
    uploaded_spike_file = st.sidebar.file_uploader("Choose Spikes/Firings File:")
    if uploaded_spike_file:
        df_spikes = pd.read_csv(uploaded_spike_file) #(uploaded_file, sep='\s+', skiprows=10, index_col = None)
        spikes_columns = len(df_spikes.columns)
        st.write('**Dataframe with Spikes - MU_Firings. There are {} Firings**'.format(spikes_columns))
        st.dataframe(df_spikes, use_container_width=True)
#---End of Insert the file with Spikes ---#

#--- Insert the file with EMG Volts Channels ---#
with col2:
    uploaded_emg_file = st.sidebar.file_uploader("Choose EMG Volts Values File:")
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
        # for i in range(1,emg_columns+1):
        #     st.write(i)
            #my_dict[i] = {"MU" +str(i)+ "_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}

        my_dict1 = {"MU1_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}
        my_dict2 = {"MU2_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}
        my_dict3 = {"MU3_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}
        my_dict4 = {"MU4_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}
        my_dict5 = {"MU5_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}
        my_dict6 = {"MU6_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}
        my_dict7 = {"MU7_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}
        my_dict8 = {"MU8_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}
        my_dict9 = {"MU9_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}
        my_dict10 = {"MU10_Firings":[], "Channel_1":[], "Channel_2":[], "Channel_3":[], "Channel_4":[]}

        #Iterate through every spike-time in Spikes file
        for spike in df_spikes.index:
            #Iterate through every time in EMG Volts Channels file
            for emgtime in df_emg.index:
                # Window for Spike-Firing 1:
                if spikes_columns >= 1:
                    #If Channel-time exists in window -10ms Spike-time +10ms, then keep spike-time and values of volts of channels
                    if df_spikes['MU1_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU1_Firings'][spike] + 0.010:
                        my_dict1["MU1_Firings"].append(df_spikes['MU1_Firings'][spike])
                        #my_dict1["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict1["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict1["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict1["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict1["Channel_4"].append(df_emg['Channel4'][emgtime])
                # Window for Spike-Firing 2:
                if spikes_columns >= 2:
                    if df_spikes['MU2_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU2_Firings'][spike] + 0.010:
                        my_dict2["MU2_Firings"].append(df_spikes['MU2_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict2["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict2["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict2["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict2["Channel_4"].append(df_emg['Channel4'][emgtime])
                # Window for Spike-Firing 3:
                if spikes_columns >= 3:
                    if df_spikes['MU3_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU3_Firings'][spike] + 0.010:
                        my_dict3["MU3_Firings"].append(df_spikes['MU3_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict3["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict3["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict3["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict3["Channel_4"].append(df_emg['Channel4'][emgtime])
                # Window for Spike-Firing 4:
                if spikes_columns >= 4:
                    if df_spikes['MU4_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU4_Firings'][spike] + 0.010:
                        my_dict4["MU4_Firings"].append(df_spikes['MU4_Firings'][spike])
                        my_dict4["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict4["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict4["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict4["Channel_4"].append(df_emg['Channel4'][emgtime])
                # Window for Spike-Firing 5:
                if spikes_columns >= 5:
                    if df_spikes['MU5_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU5_Firings'][spike] + 0.010:
                        my_dict5["MU5_Firings"].append(df_spikes['MU5_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict5["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict5["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict5["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict5["Channel_4"].append(df_emg['Channel4'][emgtime])
                # Window for Spike-Firing 6:
                if spikes_columns >= 6:
                    if df_spikes['MU6_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU6_Firings'][spike] + 0.010:
                        my_dict6["MU6_Firings"].append(df_spikes['MU6_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict6["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict6["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict6["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict6["Channel_4"].append(df_emg['Channel4'][emgtime])
                # Window for Spike-Firing 7:
                if spikes_columns >= 7:
                    if df_spikes['MU7_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU7_Firings'][spike] + 0.010:
                        my_dict7["MU7_Firings"].append(df_spikes['MU7_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict7["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict7["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict7["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict7["Channel_4"].append(df_emg['Channel4'][emgtime])
                # Window for Spike-Firing 8:
                if spikes_columns >= 8:
                    if df_spikes['MU8_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU8_Firings'][spike] + 0.010:
                        my_dict8["MU8_Firings"].append(df_spikes['MU8_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict8["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict8["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict8["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict8["Channel_4"].append(df_emg['Channel4'][emgtime])
                # Window for Spike-Firing 9:
                if spikes_columns >= 9:
                    if df_spikes['MU9_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU9_Firings'][spike] + 0.010:
                        my_dict9["MU9_Firings"].append(df_spikes['MU9_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict9["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict9["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict9["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict9["Channel_4"].append(df_emg['Channel4'][emgtime])
                # Window for Spike-Firing 10:
                if spikes_columns >= 10:
                    if df_spikes['MU10_Firings'][spike] - 0.010 <= df_emg['X [s]'][emgtime] <= df_spikes['MU10_Firings'][spike] + 0.010:
                        my_dict10["MU10_Firings"].append(df_spikes['MU10_Firings'][spike])
                        #my_dict2["Window"].append(df_emg['X [s]'][emgtime])
                        my_dict10["Channel_1"].append(df_emg['Channel1'][emgtime])
                        my_dict10["Channel_2"].append(df_emg['Channel2'][emgtime])
                        my_dict10["Channel_3"].append(df_emg['Channel3'][emgtime])
                        my_dict10["Channel_4"].append(df_emg['Channel4'][emgtime])

                

        return my_dict1, my_dict2, my_dict3, my_dict4, my_dict5, my_dict6, my_dict7, my_dict8, my_dict9, my_dict10
    
    # Get values from function, dicts for every spike:
    my_dict1, my_dict2, my_dict3, my_dict4, my_dict5, my_dict6, my_dict7, my_dict8, my_dict9, my_dict10 = create_window_spike_df()
    # Tab menu
    firing1, firing2, firing3, firing4, firing5, firing6, firing7, firing8, firing9, firing10 = st.tabs(["MU1_Firings", "MU2_Firings", "MU3_Firings","MU4_Firings","MU5_Firings","MU6_Firings","MU7_Firings","MU8_Firings","MU9_Firings","MU10_Firings"])
    
    #---- Start Firing 1 ----#
    with firing1:
        # Create dataframe from my_dict1:
        df_from_my_dict1 = pd.DataFrame(my_dict1)
        st.write('#')
        
        df_split_pivot = df_from_my_dict1.copy()
        #---Make dataframe in horizontal version:---#
        df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict1.index, 
                        columns='MU1_Firings', 
                        values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
        df_from_my_dict1 = df_from_my_dict1.unstack(level=0)
    
        df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
        # Find means for every channel:
        df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
        df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
        df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
        df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
        # Create dataframe with means:
        df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()
        # Display the tables:
        with st.expander("Show Dataframes", expanded=True):
            col1, col2 = st.columns([1,3])
            with col1:
                st.write("#")
                st.write('**Dataframe Means Values.**')
                st.write(df_split_pivot_means,  use_container_width=True)
                # Button to export the table with means:
                st.download_button(
                            label="Export Means Datatable",
                            data=df_split_pivot_means.to_csv(),
                            file_name='file_means.csv',
                            mime='text/csv',
                        )
            with col2:
                st.write("#")
                st.write('**Dataframe Split values horizontal, there are {} columns**'.format(len(df_split_pivot.columns)))
                st.dataframe(df_split_pivot, use_container_width=True)
                # Button to export the table :
                st.download_button(
                            label="Export Means Datatable",
                            data=df_split_pivot.to_csv(),
                            file_name='file_table.csv',
                            mime='text/csv',
                        )
            
        st.write("---")
        # Display the charts:
        st.subheader("**Charts for mean values per channel**")
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
        if spikes_columns>= 2:
            #if st.button('Calculate Firing 2'):   
            df_from_my_dict2 = pd.DataFrame(my_dict2)
            st.write('#')
            #st.write('**Dataframe Window -10/+10 Spike Times Vertical**', len(df_from_my_dict2.columns))
            #st.dataframe(df_from_my_dict2, use_container_width=True)

            df_split_pivot = df_from_my_dict2.copy()
            df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict2.index, 
                            columns='MU2_Firings', 
                            values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
            df_from_my_dict2 = df_from_my_dict2.unstack(level=0)
        
            df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
            df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
            df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
            df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
            df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
            
            df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()

            with st.expander("Show Dataframes", expanded=True):
                col1, col2 = st.columns([1,3])
                with col1:
                    st.write("#")
                    st.write('**Dataframe Means Values.**')
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
                    # Button to export the table :
                    st.download_button(
                                label="Export Means Datatable",
                                data=df_split_pivot.to_csv(),
                                file_name='file_table.csv',
                                mime='text/csv',
                            )
            
            st.write("---")
            st.subheader("**Charts for mean values per channel**")
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
        if spikes_columns>= 3:
            #if st.button('Calculate Firing 3'):   
            df_from_my_dict3 = pd.DataFrame(my_dict3)
            st.write('#')
            #st.write('**Dataframe Window -10/+10 Spike Times Vertical**', len(df_from_my_dict3.columns))
            #st.dataframe(df_from_my_dict3, use_container_width=True)

            df_split_pivot = df_from_my_dict3.copy()
            df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict3.index, 
                            columns='MU3_Firings', 
                            values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
            df_from_my_dict3 = df_from_my_dict3.unstack(level=0)
        
            df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
            df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
            df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
            df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
            df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
            
            df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()

            with st.expander("Show Dataframes", expanded=True):
                col1, col2 = st.columns([1,3])
                with col1:
                    st.write("#")
                    st.write('**Dataframe Means Values.**')
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
                    # Button to export the table :
                    st.download_button(
                                label="Export Means Datatable",
                                data=df_split_pivot.to_csv(),
                                file_name='file_table.csv',
                                mime='text/csv',
                            )
            
            st.write("---")
            st.subheader("**Charts for mean values per channel**")
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
        if spikes_columns>= 4:
            #if st.button('Calculate Firing 4'):   
            df_from_my_dict4 = pd.DataFrame(my_dict4)
            st.write('#')
            #st.write('**Dataframe Window -10/+10 Spike Times Vertical**', len(df_from_my_dict4.columns))
            #st.dataframe(df_from_my_dict4, use_container_width=True)

            df_split_pivot = df_from_my_dict4.copy()
            df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict4.index, 
                            columns='MU4_Firings', 
                            values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
            df_from_my_dict4 = df_from_my_dict4.unstack(level=0)
        
            df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
            df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
            df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
            df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
            df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
            
            df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()

            with st.expander("Show Dataframes", expanded=True):
                col1, col2 = st.columns([1,3])
                with col1:
                    st.write("#")
                    st.write('**Dataframe Means Values.**')
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
                    # Button to export the table :
                    st.download_button(
                                label="Export Means Datatable",
                                data=df_split_pivot.to_csv(),
                                file_name='file_table.csv',
                                mime='text/csv',
                            )
            
            st.write("---")
            st.subheader("**Charts for mean values per channel**")
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
        if spikes_columns>= 5:
            #if st.button('Calculate Firing 5'):   
            df_from_my_dict5 = pd.DataFrame(my_dict5)
            st.write('#')
            #st.write('**Dataframe Window -10/+10 Spike Times Vertical**', len(df_from_my_dict5.columns))
            #st.dataframe(df_from_my_dict5, use_container_width=True)

            df_split_pivot = df_from_my_dict5.copy()
            df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict5.index, 
                            columns='MU5_Firings', 
                            values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
            df_from_my_dict5 = df_from_my_dict5.unstack(level=0)
        
            df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
            df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
            df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
            df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
            df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
            
            df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()

            with st.expander("Show Dataframes", expanded=True):
                col1, col2 = st.columns([1,3])
                with col1:
                    st.write("#")
                    st.write('**Dataframe Means Values.**')
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
                    # Button to export the table :
                    st.download_button(
                                label="Export Means Datatable",
                                data=df_split_pivot.to_csv(),
                                file_name='file_table.csv',
                                mime='text/csv',
                            )
                
            st.write("---")
            st.subheader("**Charts for mean values per channel**")
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

    #---- Start Firing 6 ----#
    with firing6:
        if spikes_columns>= 6:
            # Create dataframe from my_dict1:
            df_from_my_dict6 = pd.DataFrame(my_dict6)
            st.write('#')
            
            df_split_pivot = df_from_my_dict6.copy()
            #---Make dataframe in horizontal version:---#
            df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict6.index, 
                            columns='MU6_Firings', 
                            values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
            df_from_my_dict6 = df_from_my_dict6.unstack(level=0)
        
            df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
            # Find means for every channel:
            df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
            df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
            df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
            df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
            # Create dataframe with means:
            df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()
            # Display the tables:
            with st.expander("Show Dataframes", expanded=True):
                col1, col2 = st.columns([1,3])
                with col1:
                    st.write("#")
                    st.write('**Dataframe Means Values.**')
                    st.write(df_split_pivot_means,  use_container_width=True)
                    # Button to export the table with means:
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
                    # Button to export the table :
                    st.download_button(
                                label="Export Means Datatable",
                                data=df_split_pivot.to_csv(),
                                file_name='file_table.csv',
                                mime='text/csv',
                            )
                
            st.write("---")
            # Display the charts:
            st.subheader("**Charts for mean values per channel**")
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
        #---- End of Start Firing 6 ----#

    #---- Start Firing 7 ----#
    with firing7:
        if spikes_columns>= 7:
            # Create dataframe from my_dict1:
            df_from_my_dict7 = pd.DataFrame(my_dict7)
            st.write('#')
            
            df_split_pivot = df_from_my_dict7.copy()
            #---Make dataframe in horizontal version:---#
            df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict7.index, 
                            columns='MU7_Firings', 
                            values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
            df_from_my_dict7 = df_from_my_dict7.unstack(level=0)
        
            df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
            # Find means for every channel:
            df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
            df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
            df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
            df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
            # Create dataframe with means:
            df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()
            # Display the tables:
            with st.expander("Show Dataframes", expanded=True):
                col1, col2 = st.columns([1,3])
                with col1:
                    st.write("#")
                    st.write('**Dataframe Means Values.**')
                    st.write(df_split_pivot_means,  use_container_width=True)
                    # Button to export the table with means:
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
                    # Button to export the table :
                    st.download_button(
                                label="Export Means Datatable",
                                data=df_split_pivot.to_csv(),
                                file_name='file_table.csv',
                                mime='text/csv',
                            )
                
            st.write("---")
            # Display the charts:
            st.subheader("**Charts for mean values per channel**")
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
            
        #---- End of Start Firing 7 ----#
    
    #---- Start Firing 8 ----#
    with firing8:
        if spikes_columns>= 8:
            # Create dataframe from my_dict1:
            df_from_my_dict8 = pd.DataFrame(my_dict8)
            st.write('#')
            
            df_split_pivot = df_from_my_dict8.copy()
            #---Make dataframe in horizontal version:---#
            df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict8.index, 
                            columns='MU8_Firings', 
                            values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
            df_from_my_dict8 = df_from_my_dict8.unstack(level=0)
        
            df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
            # Find means for every channel:
            df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
            df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
            df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
            df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
            # Create dataframe with means:
            df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()
            # Display the tables:
            with st.expander("Show Dataframes", expanded=True):
                col1, col2 = st.columns([1,3])
                with col1:
                    st.write("#")
                    st.write('**Dataframe Means Values.**')
                    st.write(df_split_pivot_means,  use_container_width=True)
                    # Button to export the table with means:
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
                    # Button to export the table :
                    st.download_button(
                                label="Export Means Datatable",
                                data=df_split_pivot.to_csv(),
                                file_name='file_table.csv',
                                mime='text/csv',
                            )
                    
            st.write("---")
            # Display the charts:
            st.subheader("**Charts for mean values per channel**")
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
            
        #---- End of Start Firing 7 ----#

     #---- Start Firing 9 ----#
    with firing9:
        if spikes_columns>= 9:
            # Create dataframe from my_dict1:
            df_from_my_dict9 = pd.DataFrame(my_dict9)
            st.write('#')
            
            df_split_pivot = df_from_my_dict9.copy()
            #---Make dataframe in horizontal version:---#
            df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict9.index, 
                            columns='MU9_Firings', 
                            values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
            df_from_my_dict9 = df_from_my_dict9.unstack(level=0)
        
            df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
            # Find means for every channel:
            df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
            df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
            df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
            df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
            # Create dataframe with means:
            df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()
            # Display the tables:
            with st.expander("Show Dataframes", expanded=True):
                col1, col2 = st.columns([1,3])
                with col1:
                    st.write("#")
                    st.write('**Dataframe Means Values.**')
                    st.write(df_split_pivot_means,  use_container_width=True)
                    # Button to export the table with means:
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
                    # Button to export the table :
                    st.download_button(
                                label="Export Means Datatable",
                                data=df_split_pivot.to_csv(),
                                file_name='file_table.csv',
                                mime='text/csv',
                            )
                
            st.write("---")
            # Display the charts:
            st.subheader("**Charts for mean values per channel**")
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
            
        #---- End of Start Firing 9 ----#

         #---- Start Firing 8 ----#
    with firing10:
        if spikes_columns>= 10:
            # Create dataframe from my_dict1:
            df_from_my_dict10 = pd.DataFrame(my_dict10)
            st.write('#')
            
            df_split_pivot = df_from_my_dict10.copy()
            #---Make dataframe in horizontal version:---#
            df_split_pivot = df_split_pivot.pivot_table(index= df_from_my_dict10.index, 
                            columns='MU10_Firings', 
                            values=['Channel_1', 'Channel_2', 'Channel_3', 'Channel_4'])
            df_from_my_dict10 = df_from_my_dict10.unstack(level=0)
        
            df_split_pivot = df_split_pivot.apply(lambda x: pd.Series(x.dropna().values))
            # Find means for every channel:
            df_split_pivot['mean_A'] = df_split_pivot['Channel_1'].mean(axis=1)
            df_split_pivot['mean_B'] = df_split_pivot['Channel_2'].mean(axis=1)
            df_split_pivot['mean_C'] = df_split_pivot['Channel_3'].mean(axis=1)
            df_split_pivot['mean_D'] = df_split_pivot['Channel_4'].mean(axis=1)
            # Create dataframe with means:
            df_split_pivot_means = df_split_pivot[['mean_A', 'mean_B', 'mean_C', 'mean_D']].copy()
            # Display the tables:
            with st.expander("Show Dataframes", expanded=True):
                col1, col2 = st.columns([1,3])
                with col1:
                    st.write("#")
                    st.write('**Dataframe Means Values.**')
                    st.write(df_split_pivot_means,  use_container_width=True)
                    # Button to export the table with means:
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
                    # Button to export the table :
                    st.download_button(
                                label="Export Means Datatable",
                                data=df_split_pivot.to_csv(),
                                file_name='file_table.csv',
                                mime='text/csv',
                            )
                
            st.write("---")
            # Display the charts:
            st.subheader("**Charts for mean values per channel**")
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
            
        #---- End of Start Firing 10 ----#


# '''
# Parameters:	
# signalneo AnalogSignal object
# 'signal' contains n analog signals.

# spiketrains : one SpikeTrain or one numpy ndarray or a list of n of either of these.
# ‘spiketrains’ contains the times of the spikes in the spiketrains.

# window : tuple of 2 Quantity objects with dimensions of time.
# 'window' is the start time and the stop time, relative to a spike, of the time interval for signal averaging. 
# If the window size is not a multiple of the sampling interval of the signal the window will be extended to the next multiple.

# '''







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


