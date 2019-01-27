var csrftoken = Cookies.get('csrftoken');
Vue.http.headers.common['X-CSRFTOKEN'] = csrftoken;

if (location.pathname == "/") {
	var topApp = new Vue({
	  delimiters: ['[[',']]'],
		el: '#topApp',
		data: {
			items: [
				{
					id: 1,
					link: '/post/development/',
					title: 'DEVELOPMENT',
					description: '개발 라이프 | 파이썬, 알고리즘, 자료구조, 웹개발 등',
					image: '/static/img/development.jpg',
				},
				{
					id: 2,
					link: '/post/workout/',
					title: 'WORKOUT',
					description: '4분할 • Calisthenics | 강해지자 | 육체가 곧 정신이다.',
					image: '/static/img/workout.jpg',
				},
				{
					id: 3,
					link: '/post/cooking/',
					title: 'COOKING',
					description: '요리 | 레시피 메모 | 세상에는 정말 많은 음식이 있다.',
					image: '/static/img/cooking.jpg',
				},
				{
					id: 4,
					link: '/contact/',
					title: 'CONTACT',
					description: '문의 | 문의에 대한 답변은 최대 하루에서 이틀이 걸립니다.',
					image: '/static/img/contact.jpg',
				},
			]
		} 
	})
};
var TaskApp = new Vue({
  delimiters: ['[[',']]'],
	el: '#tasklist',
	data: {
		tasks: [],
		newTask : {'title': null, }
	},
	mounted: function(){
		this.getTasks();
	},
	methods: {
		getTasks: function(){
			this.$http.get('/api/task/')
				.then(function(response) {
					this.tasks = response.data;
				})
				.catch(function(err) {
					console.log(err);
				})
		},
		addTask: function(){
			this.$http.post('/api/task/', this.newTask)
				.then(function(response) {
					this.getTasks();
					this.newTask = {'title': null, };
				})
				.catch(function(err) {
					console.log(err);
				})
		},
		deleteTask: function(id){
			this.$http.delete('/api/task/'+id)
				.then(function(response) {
					this.getTasks();
				})
				.catch(function(err) {
					console.log(err);
				})
		}
	}
});
if (location.pathname == "/contact/") {
	var	contactApp = new Vue({
	  delimiters: ['[[',']]'],
		el: '#contactApp',
		data: {
			alert: '',
			success: '',
			newContact: {'title': null, 'email': null, 'description': null},
		},
		methods: {
			addContact: function(){
				this.$http.post('/api/contact/', this.newContact)
					.then(function(response) {
						contactListApp.getContacts();
						this.newContact = {'title': null, 'email': null, 'description': null};
						this.success = '보냈습니다.';
						this.alert = '';
					})
					.catch(function(err) {
						console.log(err);
						this.alert = '모든 항목과 이메일을 정확히 입력해주세요.';
						this.success = '';
					})
			},
		}
	});
};

var	contactListApp = new Vue({
  delimiters: ['[[',']]'],
	el: '#contactListApp',
	data: {
		contacts: [],
	},
	mounted: function(){
		this.getContacts();
	},
	methods: {
		getContacts: function(){
			this.$http.get('/api/contact/')
				.then(function (response) {
          this.contacts = response.data;
        })
				.catch(function(err) {
					console.log(err);
				})
		},
	}
});