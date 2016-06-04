from pscore.core.wd_testcase import WebDriverTestCase
from pscore.nose2.tags import tagger
from gousto_model.pages.recipepage import RecipePage


class TestRecipePage(WebDriverTestCase):
    @tagger('RecipePage')
    def test_can_recipe_page(self):
        """
        Test Description: This is a basic test which checks whether the recipe page is
        loaded completely.

        """
        recipepage = RecipePage(self.driver).load()
        self.assertTrue(recipepage.is_loaded(), "Error loading Recipe page")

    @tagger('deliverydate')
    def test_whether_user_is_able_to_change_the_delivery_date_as_required(self):
        """
        Scenario: As a Gousto User i must be able to able to choose a delivery date to get my recipe delivered
        Test Description: This test emulates a scenario when a user selects delivery date from the list
        and checks whether the delivery date in the side panel changes accordingly.

        """
        recipepage = RecipePage(self.driver).load()
        delivery_date = recipepage.get_delivery_date()
        self.assertTrue(recipepage.check_delivery_date_matches_selected_date(delivery_date))

    @tagger('addrecipe')
    def test_whether_user_is_able_to_add_recipe_to_the_basket(self):
        """

        Scenario: As a Gousto User i should be able to add recipes to the basket
        Test Description: This test emulates a scenario when a user tries to add a recipe of their choice to the
        basket

        """
        recipepage = RecipePage(self.driver).load()
        recipepage.add_recipe()
        self.assertTrue(recipepage.check_added_recipe())

    @tagger('removerecipe')
    def test_whether_user_is_able_to_remove_recipes_from_basket(self):
        """

        Scenario: As a Gousto User i should be able to add recipes to the basket and if i want to modify the order
         i should be able to remove it from the basket

        Test Description: This test emulates a scenario when a user tries to add a recipe of their choice to the
        basket and then tries to modify the basket by removing the item added.

        """
        recipepage = RecipePage(self.driver).load()
        recipepage.add_recipe()
        recipepage.remove_recipe()

    @tagger('checkout')
    def test_user_is_able_to_checkout_after_adding_atleast_two_recipes(self):
        """

        Scenario: As a Gousto User i should be add atleast 2 recipes to the basket to be able to checkout.

        Test Description: This test emulates a scenario when a user tries to read more about the recipe.

        """
        recipepage = RecipePage(self.driver).load()
        recipepage.add_recipe()
        recipepage.add_recipe()
        recipepage.checkout()
        self.assertTrue(recipepage.checkout_page())

    @tagger('toggle-portions')
    def test_whether_user_is_able_to_toggle_portions(self):
        """
        Scenario: As a Gousto user i must be able to toggle recipes from 2 to 4.
        Test Description: This test emulates user behavior by increasing the portions by clicking on the
        toggle button

        """
        recipepage = RecipePage(self.driver).load()
        recipepage.add_recipe()
        recipepage.toggle_portions()
        self.assertTrue(recipepage.verify_portion_text(4))

    @tagger('add-portions')
    def test_whether_user_is_able_to_add_more_portions_of_checked_out_recipe(self):
        """
        Sceanario: As a Gousto user i must be able to add more portions of the recipes that have been added
        to the checked out
        Test Description: This test tries to emulate the user behavior who tries to add 2 more portions of the
        recipes that have been checked out.
        """
        recipepage = RecipePage(self.driver).load()
        recipepage.add_recipe()
        recipepage.add_two_more_portions()
        self.assertTrue(recipepage.verify_portion_text(4))

    @tagger('alert-message')
    def test_whether_user_sees_alert_message_when_trying_to_checkout_with_empty_cart(self):
        """
        Scenario: Check whether the user is able to see the alert message 
        """

        recipepage = RecipePage(self.driver).load()
        recipepage.add_recipe()
        recipepage.checkout()
        self.assertTrue(recipepage.verify_alert_message())

    @tagger('modify-portions')
    def test_whether_user_is_able_to_modify_recipe_portions(self):
        """Scenario: Check whether the user is able to modify recipe portions, the test adds 6 portions of a recipe
        and then remove one portion are resulting in 4 portions in the basket.
        """
        recipepage = RecipePage(self.driver).load()
        recipepage.add_recipe()
        recipepage.add_recipe()
        recipepage.add_recipe()
        recipepage.remove_recipe()
        self.assertTrue(recipepage.verify_portion_text(4))
