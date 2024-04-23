// // Тестовые данные для постов
// const postsData = [
//   { title: "Пост 1", content: "Содержание поста 1" },
//   { title: "Пост 2", content: "Содержание поста 2" },
//   { title: "Пост 3", content: "Содержание поста 3" },
//   { title: "Пост 4", content: "Содержание поста 4" },
//   { title: "Пост 5", content: "Содержание поста 5" },
//   { title: "Пост 6", content: "Содержание поста 6" },
//   { title: "Пост 7", content: "Содержание поста 7" },
//   { title: "Пост 8", content: "Содержание поста 8" },
//   { title: "Пост 9", content: "Содержание поста 9" },
//   { title: "Пост 10", content: "Содержание поста 10" },
//   { title: "Пост 11", content: "Содержание поста 11" },
//   // Добавьте остальные посты...
// ];

// // Функция для отображения постов на текущей странице
// function displayPosts(pageNumber) {
//   const postsPerPage = 5; // Количество постов на странице
//   const startIndex = (pageNumber - 1) * postsPerPage;
//   const endIndex = startIndex + postsPerPage;
//   const currentPagePosts = postsData.slice(startIndex, endIndex);

//   const blogPostsContainer = document.getElementById('blog-posts');
//   blogPostsContainer.innerHTML = '';
//   currentPagePosts.forEach(post => {
//       const postElement = document.createElement('div');
//       postElement.classList.add('card', 'mb-3');
//       postElement.innerHTML = `
//           <div class="card-body">
//               <h3 class="card-title">${post.title}</h3>
//               <p class="card-text">${post.content}</p>
//           </div>
//       `;
//       blogPostsContainer.appendChild(postElement);
//   });
// }

// // Функция для создания элементов пагинации
// function createPagination() {
//   const totalPages = Math.ceil(postsData.length / 5); // Постов на странице
//   const paginationContainer = document.getElementById('pagination');
//   paginationContainer.innerHTML = '';

//   for (let i = 1; i <= totalPages; i++) {
//       const pageItem = document.createElement('li');
//       pageItem.classList.add('page-item');
//       const pageLink = document.createElement('a');
//       pageLink.classList.add('page-link');
//       pageLink.href = '#';
//       pageLink.textContent = i;
//       pageLink.addEventListener('click', function(event) {
//           event.preventDefault();
//           displayPosts(i);
//           // Прокрутка к началу страницы
//           window.scrollTo({ top: 0, behavior: 'smooth' });
//       });
//       pageItem.appendChild(pageLink);
//       paginationContainer.appendChild(pageItem);
//   }
// }

// // Тестовые данные для популярных тем
// const topicsData = ["Искусственный интеллект", "Машинное обучение", "Web-разработка", "Кибербезопасность"];

// // Инициализация
// document.addEventListener('DOMContentLoaded', function() {
//   // Отображение постов на первой странице
//   displayPosts(1);
//   // Создание пагинации
//   createPagination();

//   // Заполнение популярных тем
//   const popularTopicsContainer = document.getElementById('popular-topics');
//   topicsData.forEach(topic => {
//       const topicElement = document.createElement('li');
//       topicElement.textContent = topic;
//       popularTopicsContainer.appendChild(topicElement);
//   });

//   // Инициализация слайдера
//   $('.slider').slick({
//       autoplay: true,
//       autoplaySpeed: 2000,
//       dots: true
//   });
// });
