from datapackage import Package

# Creating a new package
package = Package(base_path='C:/Users/polat/Desktop/city-water-quality-index/data')
package.infer('water.csv')

# Saving the package to 'datapackage.json'
package.save('../datapackage.json')
