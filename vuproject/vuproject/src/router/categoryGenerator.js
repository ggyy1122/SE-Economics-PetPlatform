// categoryGenerator.js
export function generateAnimalCategoryRoutes(configs) {
    return configs.map(({ pathBase, categoryName, subCategories, defaultSub }) => ({
      path: `/category/${pathBase}`,
      name: pathBase,
      redirect: `/category/${pathBase}/${defaultSub || subCategories[0]}`,
      component: () => import('@/views/categories/AnimalProductList.vue'),
      props: { categoryName },
      children: subCategories.map(sub => ({
        path: sub,
        name: `${pathBase}-${sub}`,
        component: () => import('@/views/categories/AnimalProductList.vue'),
        props: { categoryName, subCategory: sub }
      }))
    }));
  }
  