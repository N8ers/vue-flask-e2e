describe("My First Test", () => {
  it("visits the app root url", () => {
    cy.visit("/");

    cy.get("h1").should("have.text", "Vue-Flask-e2e Test!!!");
    cy.get('[data-cy="data"] > div').should("have.text", "Data: Hello, World!");

    cy.get("button").trigger("click");
    cy.get(":nth-child(4) > div").should("have.text", "TsukiGoonJoe");
  });
});
