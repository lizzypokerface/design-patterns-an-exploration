"A Director Class"
from house_builder import HouseBuilder


class IglooDirector:  # pylint: disable=too-few-public-methods
    "One of the Directors, that can build a complex representation."

    @staticmethod
    def construct():
        """Constructs and returns the final product
        Note that in this IglooDirector, it has omitted the set_number_of
        windows call since this Igloo will have no windows.
        """

        # Example of providing a method for the client to retrieve later
        # house_builder = HouseBuilder()
        # house_builder.set_building_type("Igloo")
        # house_builder.set_wall_material("Ice")
        # house_builder.set_number_doors(1)
        # return house_builder.get_result()

        return (
            HouseBuilder()
            .set_building_type("Igloo")
            .set_wall_material("Ice")
            .set_number_doors(1)
            .get_result()
        )
