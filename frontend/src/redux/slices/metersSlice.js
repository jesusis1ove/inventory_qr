import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  data: [],
};

export const metersSlice = createSlice({
  name: "meters",
  initialState,
  reducers: {
    setMeters: (state, action) => {
      state.data = action.payload;
    },
  },
});

export const { setMeters } = metersSlice.actions;
export default metersSlice.reducer;
