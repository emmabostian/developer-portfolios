import React from "react";

const Name = () => {
    return (
        <div className="flex items-center text-right h-24 max-w-[1240px] mx-auto md:mt-0 mt-10 lg:p-40 pl-0">
            <div className="flex flex-col flex-wrap gap-2 text-white text-left md:justify-start">
                <h1 className='text-left font-semibold text-5xl md:text-7xl lg:text-8xl font-serif text-white'>Ananya</h1>
                <h1 className='text-left md:pb-2 pt-1 md:pt-0 pb-3 leading-10 font-semibold text-5xl md:text-7xl lg:text-8xl font-serif'>Biswas</h1>
                
                <div className="mt-5">
                    <p className='text-left font-medium text-xl md:text-2xl lg:text-4xl font-serif text-white'>I am a passionate</p>
                    <p className='text-left font-medium text-xl md:text-2xl lg:text-4xl font-serif text-white'>frontend developer</p>
                </div>
                
            </div>
        </div>
        
    );
};

export default Name;