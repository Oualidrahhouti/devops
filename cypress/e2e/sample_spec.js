describe('Sample Test Suite', () => {
    it('Visits the Cypress example website', () => {
      // Visit the Cypress example website
      cy.visit('https://example.cypress.io')
  
      // Check if the title contains the expected text
      cy.title().should('include', 'Kitchen Sink')
  
      // Find and click on the link with the text 'type'
      cy.contains('type').click()
  
      // Find and focus on the input field with the placeholder 'type something'
      cy.get('.action-email')
        .type('hello@cypress.io')
        .should('have.value', 'hello@cypress.io')
    })
  })
  