import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { fetchPosts } from '../actions/postActions';

class Posts extends Component {
    componentWillMount(){
        this.props.fetchPosts();
    }

    componentWillReceiveProps(nextProps){ 
        if (nextProps.newPost){
            this.props.posts.unshift(nextProps.newPost); // Add new post to the beginning of the array
        }
    }

    render() {
        // Map through our posts
        const postItems = this.props.posts.map(post => (
            <div key={post.id}>
                <h3>{post.title}</h3>
                <p>{post.body}</p>
            </div>
        ));
        return (
        <div>
            <h1>Posts</h1>
            {postItems}
        </div>
        )
  }
}

Posts.propTypes = {
    fetchPosts: PropTypes.func.isRequired,
    posts: PropTypes.array.isRequired,
    newPost: PropTypes.object
}

const mapStateToProps = (state) => ({
    posts: state.posts.items,
    newPost: state.posts.item
});

export default connect(mapStateToProps, {fetchPosts})(Posts);