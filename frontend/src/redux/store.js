import { combineReducers, configureStore } from "@reduxjs/toolkit";

//import reducers
import metersReducer from "../redux/slices/metersSlice";

//import server API
import { metersAPI } from "./services/meters";

export const rootReducer = combineReducers({
  meters: metersReducer,

  //reducers
  [metersAPI.reducerPath]: metersAPI.reducer,
});

export const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) => [
    ...getDefaultMiddleware().concat(metersAPI.middleware),
  ],
});
