// This file will...
// 1 seed the db with test data
// 2 call api endpoints
// 3 check api responses agains mockRequests

// the py api server must be running for this script to work

import axios from "axios";
import _ from "lodash";
import chalk from "chalk";

import mocks from "./mockRoutes/index.js";

const baseUrl = "http://127.0.0.1:5000";

const errors = [];
const routesThat404 = [];

// For Each Mock Endpoint
for (const route in mocks) {
  // For Each REST Method of Each Endpoint
  for (const requestMethod in mocks[route]) {
    // For Each Route of Each Method
    for (const endpoint in mocks[route][requestMethod]) {
      const mockedResponse = mocks[route][requestMethod][endpoint].data;
      let apiResponse;

      try {
        const response = await axios({
          method: requestMethod,
          baseURL: baseUrl,
          url: endpoint,
          mode: "no-cors",
          headers: {
            "Content-Type": "application/json",
          },
        });
        apiResponse = response.data;
      } catch (error) {
        routesThat404.push({ route, endpoint, requestMethod });
      }

      if (apiResponse) {
        const mockAndApiMatch = _.isEqual(mockedResponse, apiResponse);
        if (!mockAndApiMatch) {
          errors.push({ route, endpoint, requestMethod });
        }
      }
    }
  }
}

if (errors.length || routesThat404.length) {
  if (errors.length) {
    console.log(
      chalk.white.bgRed.bold(
        "*** Mocks and API response do not match for the following: ***"
      )
    );
    for (const error of errors) {
      console.log(error);
    }
  }

  if (routesThat404.length) {
    console.log(
      chalk.white.bgRed.bold(
        "*** The following routes returned 404, make sure the API endpoint exists: ***"
      )
    );
    for (const error of routesThat404) {
      console.log(error);
    }
  }
} else {
  console.log(chalk.blue("All Mock Requests match the API's response!"));
}

// TODO:
// * add an error message for axios failures 'make sure api server is running'
// * if any mocks fail, message saying 'make sure db is seeded properly'
// * It would be super cool if we could automate an update of the mock :thinking-emoji
