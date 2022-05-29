// This file will...
// 1 seed the db with test data
// 2 call api endpoints
// 3 check api responses agains mockRequests

// the py api server must be running for this script to work

import axios from "axios";
import _ from "lodash";

// mockRequests could be broken into blueprints
import { hello, friend } from "./mockRoutes/index.js";

const baseUrl = "http://127.0.0.1:5000";

const errors = [];

for (const requestMethod in hello) {
  for (const endpoint in hello[requestMethod]) {
    const mockedResponse = hello[requestMethod][endpoint].data;

    const apiResponse = await axios({
      method: requestMethod,
      baseURL: baseUrl,
      url: endpoint,
      mode: "no-cors",
      headers: {
        "Content-Type": "application/json",
      },
    });

    const mockAndApiMatch = _.isEqual(mockedResponse, apiResponse.data);
    if (!mockAndApiMatch) {
      errors.push({ endpoint: endpoint, method: requestMethod });
    }
  }
}

if (errors.length) {
  // It would be super cool if we could automate an update of the mock :thinking-emoji
  // It'd be cool to add chalk.js so we can color code the errors
  console.log("*** MOCK & API DO NOT MATCH THE FOLLOWING ROUTES: ***");
  for (const error of errors) {
    console.log("error ", error);
  }
}
