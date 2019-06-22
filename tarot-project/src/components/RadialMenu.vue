<template>
    <div>
        <div :style="wrapperStyle" class="radial-menu-wrapper">
        <div
            :class="['radial-menu-container', shouldOpen && 'open']"
            :style="containerStyle"
            @click="handleClick">+</div>
        <slot v-if="shouldOpen"></slot>
        </div> 
    </div>
</template>

<style scoped>
.radial-menu-wrapper {
	position:absolute;
	user-select: none;
	border-radius: 50%;
	font-size: 32px;
	font-weight: bold;
	border-radius: 50%;
	box-shadow: 0 1px 3px rgba(0, 0, 0, 0.24), 0 0 0 rgba(0, 0, 0, 0.16);
    justify-content: center;
    align-items: center;
}
.radial-menu-container {
	background-color: white;
	display: flex;
	justify-content: center;
	align-items: center;
	border-radius: 50%;
	transition: all 0.2s ease;
	position: relative;
	z-index: 6;
}
.radial-menu-container.open {
	transform: rotateZ(45deg);
}
</style>

<script>
import RadialMenuItem from './RadialMenuItem';

export default {
    name: 'RadialMenu',
    props: {
        angleRestriction: {type:Number, default:180},
        size: { type: Number, default: 20 },
		itemSize: { type: Number, default: 50 },
		rotate: { type: Number, default: 0 },
		radius: { type: Number, default: 30 },
		open: { type: Boolean, default: undefined }     // event variable to open or close the menu?
    },
    data(){
        const { size } = this;
        const manualMode = typeof this.open !== 'undefined';
        return {
            manualMode,
            isOpen:false,       // open/closed state variable
            wrapperStyle: {
				margin: (30 - size/2) + 'vw ' + (50-size/2) + 'vw'
			},
			containerStyle:{
				width: size + 'vw',
				height: size + 'vw'
			}

        }
    },
    computed:{
        shouldOpen(){
            const {open, manualMode, isOpen} = this;
            return manualMode ? open : isOpen;
		},
    },
    mounted() {
		document.addEventListener('click', this.closeMenuEvent);
		this.setChildProps();
	},
	beforeUpdate() {
		this.setChildProps();
	},
	beforeDestroy() {
		document.removeEventListener('click', this.closeMenuEvent);
    },
    methods: {
        closeMenuEvent(e) {
			if (this.shouldOpen && !this.$el.contains(e.target)) {
				this.toggleMenu();
			}
        },
        handleClick() {
			this.$emit('radialClick');
			this.toggleMenu();
        },
        toggleMenu() {
			if (this.manualMode) return;
			if (this.isOpen) {
				this.isOpen = false;
				this.$emit('close');
			} else {
				this.isOpen = true;
				this.$emit('open');
			}
        },
        setChildProps() {
			// Manually add prop data to the items
			const items = this.$slots.default.map(s => s.componentOptions.propsData);
			const { size, itemSize, angleRestriction, rotate, radius } = this;
			const angle =
				angleRestriction > 300 || angleRestriction < -300 ? 360 : angleRestriction;
			const frags = angle / (items.length || 1);
			const angles = items.map(
				(item, index) => (Math.PI * (frags * index + rotate)) / 180
			);
			console.log(angles);
			items.forEach((propData, index) => {
				propData.width = itemSize;
				propData.height = itemSize;
				propData.left =
					(size / 2 + Math.cos(angles[index]) * radius - itemSize / 2); // -1 to have the items in the right order
				propData.top = size / 2 - Math.sin(angles[index]) * radius - itemSize / 2;
				propData.onClick = this.manualMode ? null : this.toggleMenu; // To prevent double emiting click event
			});
		}
    }
}
</script>
