# mocks

This folder holds mock responses for the vue-app vitest tests.

It also contains a `confirmMocks.js` file. This file will make a network request with each corrisponding mock response. It will compaire the results of the API response with the mock responses, and flag incorrect mocks. This is to ensure mock response stay accurate to the existing API.

This also means that the seed data must be kept up to date with any API changes and database migrations.

### To run `confirmMocks.js`

1. Make sure the database has been seeded with test data
1. Start the flask API (it has a read me)
1. Run `npm run confirm`
