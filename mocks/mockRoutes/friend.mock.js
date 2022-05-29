export default {
  get: {
    "/friend": {
      data: [
        { id: 1, name: "Tsuki" },
        { id: 2, name: "Goon" },
        { id: 3, name: "Joe" },
      ],
    },
    "/friend/1": {
      data: [{ id: 1, name: "Tsuki" }],
    },
    "/friend/2": {
      data: [{ id: 2, name: "Goon" }],
    },
    "/friend/3": {
      data: [{ id: 3, name: "Joe" }],
    },
  },
};
